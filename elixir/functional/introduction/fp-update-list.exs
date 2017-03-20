defmodule Solution do
  defp printlist([num|numlist]) do
    num
    |> String.trim("\n")
    |> String.to_integer
    |> abs
    |> IO.puts

    printlist(numlist)
  end
  defp printlist([]) do
    System.halt(0)
  end
  def getlist(numlist) do
    num = IO.gets ""
    if num != :eof do
      getlist([num|numlist])
    else
      numlist
      |> Enum.reverse
      |> printlist
    end
  end
end

Solution.getlist([])