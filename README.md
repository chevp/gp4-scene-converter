# Quantum Rift Scene Converter

This project is the **Scene Converter** component for **Quantum Rift**, built using **Quarkus** and **Java**. The `SceneConverterMain` class serves as the entry point for this Quarkus application. It interacts with a service to process scene data and provides a command-line interface to pass arguments.

## Features

- **Command-line Interface (CLI)**: Accepts arguments and processes them using the `SceneConverterService`.
- **Quarkus Framework**: Utilizes Quarkus for fast startup times and low memory footprint, making it ideal for cloud-native applications.
- **Dependency Injection**: Leverages CDI for injecting the `SceneConverterService` into the main application class.
  
## Requirements

- **Java** (>=11)
- **Maven** (>=3.x)
- **Quarkus** (>=2.x)

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/chevp/quantum-rift-scene-converter.git
cd quantum-rift-scene-converter
```

### 2. Install dependencies:

```bash
./mvnw clean install
```

### 3. Run the application:

```bash
./mvnw quarkus:dev
```

Alternatively, you can run the application directly using:

```bash
java -jar target/quarkus-app/quarkus-run.jar
```

### Command-line usage:

To run the `SceneConverterMain` with arguments:

```bash
java -jar target/quarkus-app/quarkus-run.jar [your_scene_arguments]
```

If no arguments are provided, it will use the default message `commando`.

## Example:

```bash
java -jar target/quarkus-app/quarkus-run.jar "Quantum Rift Scene Conversion"
```

This will output:

```
Hello, Quantum Rift Scene Conversion
```

If no arguments are provided, it will output:

```
Hello, commando
```

## Folder Structure

```
├── src/                          # Source code
│   ├── main/                     # Main application code
│   │   └── java/org/gp4/sceneconverter/  # Scene converter package
│   └── test/                     # Test cases
├── pom.xml                       # Maven project file
├── target/                       # Compiled application output
└── README.md                     # This README file
```

## Development

To develop and test the application in real-time with Quarkus:

```bash
./mvnw quarkus:dev
```

This will start the application in development mode, allowing hot reload and live testing of changes.

## License

This project is licensed under the MIT License.
