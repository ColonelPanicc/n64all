package com.colonelpanic.n64all.server

import com.colonelpanic.n64all.server.service.ControllerService
import com.google.inject.Guice
import com.google.inject.Inject
import com.google.inject.Injector
import com.google.inject.Module
import io.vertx.core.AbstractVerticle
import io.vertx.core.Vertx
import io.vertx.ext.web.Router
import io.vertx.ext.web.RoutingContext
import java.util.concurrent.atomic.AtomicInteger

/**
 * A VertX Verticle to serve up the Player-based controls as a REST api.
 *
 * @param controllerService the implementation of the controller service, to manage controller state
 */
class PlayerVerticle @Inject constructor(private val controllerService: ControllerService) : AbstractVerticle() {
    private val playerCounter: AtomicInteger = AtomicInteger(0)

    private fun join(context: RoutingContext) {
        TODO("Need to implement the joining of rooms as before")
    }

    private fun leave(context: RoutingContext) {
        TODO("Leave the room needs to be implemented as a route")
    }

    private fun update(context: RoutingContext) {
        TODO("Need to add update state as a route")
    }

    private fun getState(context: RoutingContext) {
        val response = context.response()
        response?.putHeader("content-type", "text/html")?.end("<h1>Test</h1>")
    }

    override fun start() {
        val router = Router.router(vertx)

        router.route("/state").handler(this::getState)
        router.route("/join").handler(this::join)
        router.route("/leave").handler(this::leave)
        router.route("/update").handler(this::update)

        vertx.createHttpServer()
                .requestHandler(router::accept)
                .listen(config().getInteger("http.port", 8080))

    }
}

fun main() {
    // Create a Guice injector to do inversion of control
    val injector = Guice.createInjector(ServerModule())

    // start the service
    val instance = injector.getInstance(PlayerVerticle::class.java)
    val vertx = injector.getInstance(Vertx::class.java)

    vertx.deployVerticle(instance)
}