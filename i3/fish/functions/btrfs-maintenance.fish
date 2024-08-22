function btrfs-maintenance
  sudo /usr/share/btrfsmaintenance/btrfs-scrub.sh
  sudo /usr/share/btrfsmaintenance/btrfs-trim.sh
  sudo /usr/share/btrfsmaintenance/btrfs-balance.sh
  sudo /usr/share/btrfsmaintenance/btrfs-defrag.sh
  sudo btrfs balance start -m /
  sudo btrfs filesystem defragment -r /
end
