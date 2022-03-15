###Creating Object Array
Add-Type -AssemblyName System.Windows.Forms

###Creating Main Form to House Program
$mainForm = New-Object System.Windows.Forms.Form
$mainForm.Text = "Admin_Quick GUI"
$mainForm.Width = 600
$mainForm.Height = 400
$mainForm.AutoSize = $True

###Creating Form label
$label1 = New-Object System.Windows.Forms.label
$label1.Text = "1. Create User"
$label1.Location = New-Object System.Drawing.Point(10,10)
$label1.AutoSize = $True
$mainForm.Controls.Add($label1)

###Creating Form label
$label2 = New-Object System.Windows.Forms.label;
$label2.Text = "2. Modify User"
$label2.Location = New-Object System.Drawing.Point(10,40)
$label2.AutoSize = $True
$mainForm.Controls.Add($label2)

###Creating Form label
$label3 = New-Object System.Windows.Forms.label
$label3.Text = "3. Delete User"
$label3.Location = New-Object System.Drawing.Point(10,70)
$label3.AutoSize = $True
$mainForm.Controls.Add($label3)

###Creates Targeted File List in Drop Down
$dropDown = New-Object System.Windows.Forms.ComboBox
$dropDown.Items.Add($label1.Text)
$dropDown.Items.Add($label2.Text)
$dropDown.Items.Add($label3.Text)
$dropDown.Location  = New-Object System.Drawing.Point(250,10)
$dropDown.Width = 300
$dropDown.Width = 400
$dropDown.Height = 20
$mainForm.Controls.Add($dropDown)

###Button to Engage User
$Button = New-Object System.Windows.Forms.Button
$Button.Location = New-Object System.Drawing.Size(540,390)
$Button.Size = New-Object System.Drawing.Size(120,23)
$Button.Text = "Confirm Choice"
$mainForm.Controls.Add($Button)

#####Money Move Area to tie Functions in
###Button Code to Execute desired Function
$Button.Add_Click(
{
if ($dropDown.SelectedItem -eq $label1.Text) {
    Write-Host "Yeet 1"
    }
if ($dropDown.SelectedItem -eq $label2.Text) {
    Write-Host "Yeet 2"
    }
if ($dropDown.SelectedItem -eq $label3.Text) {
    Write-Host "Yeet 3"
    }
}
)

#Must be LAST GUI Line
$mainForm.ShowDialog()

