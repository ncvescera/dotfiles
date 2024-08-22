function ollama
  if test "$(docker ps --filter 'name=ollama' --filter 'status=running' --quiet)" = ""
    echo "Starting docker container ..."
    docker start ollama
  end

  docker exec -it ollama ollama run $argv
end
