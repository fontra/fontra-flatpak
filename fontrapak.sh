#!/usr/bin/env bash 
# Workaround for flatpak 1.16+ sandbox /tmp restrictions
export TMPDIR="${XDG_CACHE_HOME:-$HOME/.cache}"
mkdir -p "$TMPDIR"

exec /app/bin/fontrapak-bin "$@"
