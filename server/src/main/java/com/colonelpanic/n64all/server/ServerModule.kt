package com.colonelpanic.n64all.server

import com.colonelpanic.n64all.server.model.ControllerState
import com.colonelpanic.n64all.server.service.ControllerService
import com.google.inject.AbstractModule
import com.google.inject.Provider
import com.google.inject.Provides
import com.google.inject.Singleton
import io.vertx.core.Vertx

class ServerModule : AbstractModule() {
    override fun configure() {
        bind(ControllerService::class.java).asEagerSingleton()
        bind(PlayerVerticle::class.java).asEagerSingleton()
        bind(StateFactory::class.java).asEagerSingleton()
        bind(ControllerState::class.java)
    }

    @Provides
    @Singleton
    fun provideVertx(): Vertx {
        return Vertx.vertx()
    }

}