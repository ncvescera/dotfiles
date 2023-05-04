function ssh-mem
  eval $(ssh-agent -c)
  ssh-add
end
