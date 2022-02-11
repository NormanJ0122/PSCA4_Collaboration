###Creating Object Array
Add-Type -AssemblyName System.Windows.Forms

###Creating Main Form to House Program
$mainForm = New-Object System.Windows.Forms.Form
$mainForm.Text = "Test GUI for Program Expansion"
$mainForm.Width = 600
$mainForm.Height = 400
$mainForm.AutoSize = $True

###Creating Form label
$label = New-Object System.Windows.Forms.label
$label.Text = "Available Files"
$label.Location = New-Object System.Drawing.Point(10,10)
$label.AutoSize = $True
$mainForm.Controls.Add($label)

###Creates Targeted File List in Drop Down
$dropDown = New-Object System.Windows.Forms.ComboBox
$dropDown.Width = 300
$moveLocation = Read-Host -Prompt "Provide filepath to files:  "
Set-Location -Path $moveLocation
Write-Host "
Changing current directory.
"
Read-Host -Prompt "Press Enter to Continue.
"
Get-ChildItem
Write-Host "
Files in current directory.
"
$fileList = Get-ChildItem
Foreach ($file in $fileList)
{

$dropDown.Items.Add($file)
}
$dropDown.Location  = New-Object System.Drawing.Point(250,10)
$dropDown.Width = 400
$dropDown.Height = 20
$mainForm.Controls.Add($dropDown)

###Information label
$label2 = New-Object System.Windows.Forms.label
$label2.Text = "New format will display here:"
$label2.Location  = New-Object System.Drawing.Point(10,40)
$label2.AutoSize = $true
$mainForm.Controls.Add($label2)

###Object to Hold New File Format
$label3 = New-Object System.Windows.Forms.label
$label3.Text = ""
$label3.Location  = New-Object System.Drawing.Point(200,40)
$label3.AutoSize = $true
$mainForm.Controls.Add($label3)

###Button to Click to Format
$Button = New-Object System.Windows.Forms.Button
$Button.Location = New-Object System.Drawing.Size(540,390)
$Button.Size = New-Object System.Drawing.Size(120,23)
$Button.Text = "Format"
$mainForm.Controls.Add($Button)

###Formatting Code Tied to Button
$Button.Add_Click(
{
$modObj = GCI -Filter $dropDown.SelectedItem
$part1 = $modObj.BaseName
$part2 = $modObj.Extension
$part1 = $part1.Replace('.','_')
$part3 = $part1 + $part2
Rename-Item $modObj -NewName $part3
$label3.Text = $part3
}
)
$mainForm.ShowDialog() #Must be LAST GUI Line