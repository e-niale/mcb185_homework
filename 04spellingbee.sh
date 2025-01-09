gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -v "[^zoniarc]" | grep ".*r.*" | grep -E ".{4,}"
