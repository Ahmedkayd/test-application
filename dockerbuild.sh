#!/bin/bash
set -e

REPO="ahismail/test-app"
DOCKERFILE="Dockerfile"
DATE=$(date -u +"%Y-%m-%d")
GIT_SHORT_SHA="${TAG:-}"

# Get existing tags
EXISTING_TAGS=$(docker images "$REPO" --format "{{.Tag}}" | grep -E "^$DATE-[0-9]+$" || true)

case "$EXISTING_TAGS" in
  "")
    SUFFIX=1
    ;;
  *)
    SUFFIX=$(echo "$EXISTING_TAGS" | sed -E "s/^$DATE-([0-9]+)$/\1/" | sort -n | tail -1)
    SUFFIX=$((SUFFIX + 1))
    ;;
esac

IMAGE_TAG="$DATE-$SUFFIX"
if [ -n "$GIT_SHORT_SHA" ]; then
  IMAGE_TAG="$DATE-${GIT_SHORT_SHA}-$SUFFIX"
fi

IMAGE="$REPO:$IMAGE_TAG"

echo "Building Docker image: $IMAGE" >&2  
docker build -f "$DOCKERFILE" -t "$IMAGE" .

echo "✅ Build complete: $IMAGE" >&2  

# Output the tag to stdout (for capture)
echo "$IMAGE_TAG" 
