# This doesn't work don't know why

defmodule Solution do
  def gcd(a,0), do: abs(a)
  def gcd(a,b), do: gcd(b, rem(a,b))
  def mulall(list) do
    mulall(list,1)
  end
  def mulall([num|tail], acc) do
    mulall(tail,acc*num)   
  end
  def mulall([],acc) do
    acc
  end
end

_ = IO.gets ""
fl = IO.gets ""
_ = IO.gets ""
sl = IO.gets ""

firstline = Enum.map(fl |> String.trim("\n") |> String.split(" "), &String.to_integer/1) |> Solution.mulall |> rem(1000000007)
secondline = Enum.map(sl |> String.trim("\n") |> String.split(" "), &String.to_integer/1) |> Solution.mulall |> rem(1000000007)

IO.puts firstline
IO.puts secondline

IO.puts Solution.gcd(firstline,secondline) 


