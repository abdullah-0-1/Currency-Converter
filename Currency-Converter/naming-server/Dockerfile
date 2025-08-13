# Use Java 21 base image
FROM eclipse-temurin:21-jdk-alpine

# Set working directory
WORKDIR /app

# Copy built JAR
COPY target/namingserverv1.jar app.jar

# Run the app
ENTRYPOINT java -jar app.jar