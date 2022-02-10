$list = ("Research","Integration","Testing")

ForEach ($i in $list) {
    $Path = "ou=" + "$i" + ",ou=IT,dc=HUNT,dc=com"
    New-ADGroup $i -GroupCategory Security -GroupScope Global -DisplayName $i -Path $Path 
    Write-Host $i
    }