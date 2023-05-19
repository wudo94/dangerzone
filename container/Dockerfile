FROM alpine:latest

ARG TESSDATA_VERSION=4.1.0
ARG TESSDATA_CHECKSUM=990fffb9b7a9b52dc9a2d053a9ef6852ca2b72bd8dfb22988b0b990a700fd3c7

# Install dependencies
RUN apk -U upgrade && \
    apk add \
    ghostscript \
    graphicsmagick \
    libreoffice \
    openjdk8 \
    poppler-utils \
    poppler-data \
    python3 \
    py3-magic \
    tesseract-ocr

RUN mkdir tessdata && cd tessdata \
    && wget https://github.com/tesseract-ocr/tessdata/archive/$TESSDATA_VERSION/tessdata-$TESSDATA_VERSION.tar.gz \
    && echo "$TESSDATA_CHECKSUM  tessdata-$TESSDATA_VERSION.tar.gz" | sha256sum -c \
    && tar -xzvf tessdata-$TESSDATA_VERSION.tar.gz -C . \
    && find . -name '*.traineddata' -maxdepth 2 -exec cp {} /usr/share/tessdata \; \
    && cd .. && rm -r tessdata

COPY dangerzone.py /usr/local/bin/
RUN chmod +x /usr/local/bin/dangerzone.py

# Add the unprivileged user
RUN adduser -s /bin/sh -D dangerzone
USER dangerzone

# /tmp/input_file is where the first convert expects the input file to be, and
# /tmp where it will write the pixel files
#
# /dangerzone is where the second script expects files to be put by the first one
#
# /safezone is where the wrapper eventually moves the sanitized files.
VOLUME /dangerzone /tmp/input_file /safezone
