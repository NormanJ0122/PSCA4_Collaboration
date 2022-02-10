$csvfile = "C:\Users\Administrator\Documents\Scripts\OUmap.csv"
$OUs = Import-CSV $csvfile
New-ADOrganizationalUnit IT -DisplayName IT

ForEach ($i in $OUs) {
    $OU = $i.OrganUnit
    $Path = "ou=IT,dc=HUNT,dc=com"
    New-ADOrganizationalUnit $OU -DisplayName $OU -Path $Path
    }

$list = ("Research","Integration","Testing")

ForEach ($i in $list) {
    $Path = "ou=" + "$i" + ",ou=IT,dc=HUNT,dc=com"
    New-ADGroup $i -GroupCategory Security -GroupScope Global -DisplayName $i -Path $Path 
    Write-Host $i
    }

$csvfile = "C:\Users\Administrator\Documents\Scripts\usermap.csv"
$users = Import-CSV $csvfile

ForEach ($i in $users) {
	$DisplayName = $i.First + " " + $i.Last
   $SecurePass = ConvertTo-SecureString $i.Password -AsPlainText -Force
	$UPN = $i.Last + $i.Init
    $Email = $UPN.ToLower() + "@HUNT.com"
    $Path = "ou=" + $i.Department + ",ou=IT,dc=HUNT,dc=com"
	New-ADUser -Name $DisplayName -Given $i.First -Surname $i.Last -DisplayName $DisplayName -UserPrincipalName $UPN -Department $i.Department -EmailAddress $Email -Path $Path -AccountPassword $SecurePass -PasswordNeverExpires $true -CannotChangePassword $true -Enabled $true
}

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
