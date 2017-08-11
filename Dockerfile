from netflixoss/genie-app:3.0.11
MAINTAINER Gary Schulte <gary.schulte@opengov.com>

#these args must be passed for s3 to work
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

RUN test -n "$AWS_ACCESS_KEY_ID"
RUN test -n "$AWS_SECRET_ACCESS_KEY"

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

RUN sh -c 'mkdir -p /etc/genie ; echo "accessKey=$AWS_ACCESS_KEY_ID\nsecretKey=$AWS_SECRET_ACCESS_KEY" >/etc/genie/creds.props'

ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-cp", "/usr/local/bin/genie.jar:/etc/genie/", "org.springframework.boot.loader.PropertiesLauncher", "--genie.aws.credentials.file=/creds.props", "--spring.profiles.active=dev,s3"]
