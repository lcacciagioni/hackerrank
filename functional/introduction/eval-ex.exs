defmodule Solution do
  defp fact(0) do
    1
  end
  defp fact(num) when num > 0 do
    num * fact(num - 1)
  end
  defp calculateex(0, _, _) do
    IO.puts 1.0
  end
  defp calculateex(x, acc, iteration) when iteration >= 0 and iteration < 10 do
    pow = :math.pow(x, iteration)
    factor = fact(iteration) / 1
    value = pow / factor
    calculateex(x, value + acc, iteration + 1)
  end
  defp calculateex(_, acc, iteration) when iteration == 10 do
    acc
    |> Float.round(4)
    |> IO.puts
  end

  defp printlist([x|tail]) do
    newx = x 
      |> String.trim("\n")
      |> String.to_float

    calculateex(newx, 0.0, 0)
    printlist(tail)
  end
  defp printlist([]) do
     System.halt(0)
  end

  def getlist(currlist) do
    num = IO.gets ""
    if num != :eof do
      getlist([num|currlist])
    else
      printlist(currlist |> Enum.reverse)
    end
  end
end

_ = IO.gets ""
Solution.getlist([])