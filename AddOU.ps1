$csvfile = "C:\Users\Administrator\Documents\Scripts\OUmap.csv"
$OUs = Import-CSV $csvfile
New-ADOrganizationalUnit IT -DisplayName IT

ForEach ($i in $OUs) {
    $OU = $i.OrganUnit
    $Path = "ou=IT,dc=HUNT,dc=com"
    New-ADOrganizationalUnit $OU -DisplayName $OU -Path $Path
    }