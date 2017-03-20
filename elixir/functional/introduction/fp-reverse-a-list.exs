defmodule Solution do
  defp printlist([num|tail]) do
    num
    |> String.trim("\n")
    |> IO.puts

    printlist(tail)
  end
  defp printlist([]) do
    System.halt(0)
  end

  def getlist(numlist) do
    num = IO.gets ""
    if num != :eof do
      getlist([num|numlist])
    else
      printlist(numlist)
    end
  end

end

Solution.getlist([])