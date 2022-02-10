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