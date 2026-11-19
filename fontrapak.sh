#!/bin/sh
# Workaround for flatpak 1.16+ sandbox /tmp restrictions
export TMPDIR="${XDG_CACHE_HOME:-$HOME/.cache}"
mkdir -p "$TMPDIR"

exec python3 /app/share/fontrapak/FontraPakMain.py "$@"
