package com.colonelpanic.n64all.server

import io.vertx.core.AbstractVerticle
import io.vertx.core.Vertx
import io.vertx.ext.web.Router

class PlayerVerticle : AbstractVerticle() {
    override fun start() {
        val router = Router.router(vertx)

        router.route("/").handler {
            val response = it?.response()
            response?.putHeader("content-type", "text/html")?.end("<h1>Test</h1>")
        }

        vertx.createHttpServer()
                .requestHandler(router::accept)
                .listen(config().getInteger("http.port", 8080))
    }
}

fun main() {
    val vertx = Vertx.vertx()
    vertx.deployVerticle(PlayerVerticle())
}