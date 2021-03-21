#!/bin/bash
BRANCH="$GIT_LOCAL_BRANCH"
COMMIT_ID="$GIT_COMMIT"

TAGNAME="${COMMIT_ID}"


IMAGETAG="josecarlosme/tungsteno:$TAGNAME"

docker build -t $IMAGETAG ./
docker push $IMAGETAG

if [[ "$BRANCH" == "master" ]]; then
    docker tag $IMAGETAG josecarlosme/tungsteno:latest
    docker push josecarlosme/tungsteno:latest
fi

IMAGETAG_DOCS="josecarlosme/tungsteno-docs:$TAGNAME"

docker build -t $IMAGETAG_DOCS ./docs
docker push $IMAGETAG_DOCS

if [[ "$BRANCH" == "master" ]]; then
    docker tag $IMAGETAG_DOCS josecarlosme/tungsteno-docs:latest
    docker push josecarlosme/tungsteno-docs:latest
fi
