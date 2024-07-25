package org.gp4.sceneconverter;

import jakarta.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class SceneConverterService {

    public String greeting(String name) {
        return "hello " + name;
    }

}
