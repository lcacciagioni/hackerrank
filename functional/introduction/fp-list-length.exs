defmodule Solution do
  def getlist(count) do
    num = IO.gets ""
    if num != :eof do
      getlist(count + 1)
    else
      IO.puts count
    end
  end
end

Solution.getlist(0)