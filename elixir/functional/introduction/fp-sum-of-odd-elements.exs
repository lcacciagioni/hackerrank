defmodule Solution do
  require Integer

  def getlist(totalsum) do
    num = IO.gets ""
    if num != :eof do
      finalnum = num 
        |> String.trim("\n")
        |> String.to_integer
      if Integer.is_odd(finalnum) do
        getlist(finalnum + totalsum)
      else
        getlist(totalsum)
      end
    else
      IO.puts totalsum
    end
  end
end

Solution.getlist(0)