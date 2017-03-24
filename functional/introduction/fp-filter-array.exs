defmodule Solution do
  defp printnum(belownum) do
    num = IO.gets ""
    if num != :eof do
      if (num |> String.trim("\n") |> String.to_integer) < belownum do
        num
        |> String.trim("\n")
        |> IO.puts
      end
      printnum(belownum)
    end
  end
  
  def start do
    belowstr = IO.gets ""
    belownum =  belowstr |> String.trim("\n") |> String.to_integer
    printnum(belownum)
  end
end

Solution.start