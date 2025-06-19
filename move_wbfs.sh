#!/bin/bash

SRC_DIR="$(pwd)"
DEST="/run/media/bhu2/WII/wbfs"

mkdir -p "$DEST"

for file in "$SRC_DIR"/*.wbfs; do
  [[ -e "$file" ]] || continue
  
  fname="$(basename -- "$file")"
  
  if [[ "$fname" =~ ^(.+)\ \[([A-Z0-9]{6})\]\.wbfs$ ]]; then
    title="${BASH_REMATCH[1]}"
    gameid="${BASH_REMATCH[2]}"
    
    clean_title="${title//\'/}"

    out_dir="$DEST/$clean_title [$gameid]"
    mkdir -p "$out_dir"
    echo "Copying: $fname → $out_dir/$gameid.wbfs"
    rsync -ah --progress "$file" "$out_dir/$gameid.wbfs"
  else
    echo "Skipping: $fname (doesn't match pattern)"
  fi
done
