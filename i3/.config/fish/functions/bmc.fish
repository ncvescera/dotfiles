function bmc
  ssh -t <username>@baioXeon "sudo systemctl $argv redir.service"
end
