$csvfile = "C:\Users\Administrator\Documents\Scripts\usermap.csv"
$users = Import-CSV $csvfile

ForEach ($i in $users) {
    $DisplayName = $i.First + " " + $i.Last
    if ($i.Department -eq "Integration") {
        Add-ADGroupMember "Integration" -Members $DisplayName
        }
    if ($i.Department -eq "Research") {
        Add-ADGroupMember "Research" -Members $DisplayName
        }
    if ($i.Department -eq "Testing") {
        Add-ADGroupMember "Testing" -Members $DisplayName
        }
        }
