function bmc
  ssh -t vescera@baioXeon "sudo systemctl $argv redir.service"
end
