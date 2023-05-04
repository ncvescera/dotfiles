function uninstall
  paru -Rcns $argv
end

function safe_uninstall
  paru -Runs $argv
end
