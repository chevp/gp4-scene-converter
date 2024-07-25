package org.gp4.sceneconverter;

import jakarta.inject.Inject;

import io.quarkus.runtime.QuarkusApplication;
import io.quarkus.runtime.annotations.QuarkusMain;

@QuarkusMain
public class SceneConverterMain implements QuarkusApplication {

    @Inject
    SceneConverterService service;

    @Override
    public int run(String... args) {

        if(args.length>0) {
            System.out.println(service.greeting(String.join(" ", args)));
        } else {
            System.out.println(service.greeting("commando"));
        }

        return 0;
    }
}
