#! perl.exe

open(RD, "Artist_lists_small_big.csv");

$a='Led Zeppelin';
$b='The Beatles';

$cnt = 1;
while(<RD>)
{
    if ($_ =~ m/.*$a.*$b.*/imsg)
    {
    print("1: matched at line $.");
    # print($_);
    $cnt++;
    }

    if ($_ =~ m/.*$b.*$a/imsg)
    {
    print("2: matched at line $.");
    # print($_);
    $cnt++;
    }

}
print $cnt;