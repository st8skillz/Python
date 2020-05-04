Public Class DroneDogsOrder

    Private Sub btnCalculate_Click(sender As Object, e As EventArgs) Handles btnCalculate.Click

        'Declare constants
        Const DBL_SALES_TAX_RATE As Double = 0.07
        Const DBL_DRONE_DOG_PRICE As Double = 1.99

        'Declare variables 
        Dim intNumBeefDogs As Integer
        Dim intNumPorkDogs As Integer
        Dim intNumTurkeyDogs As Integer
        Dim intNumTotalDogs As Integer
        Dim dblSubTotal As Double
        Dim dblTotalSalesTax As Double
        Dim dblTotalCost As Double

        'Extract user typed quantities from text boxes and convert to integers
        intNumBeefDogs = Convert.ToInt32(txtBeefDogs.Text)
        intNumPorkDogs = Convert.ToInt32(txtPorkDogs.Text)
        intNumTurkeyDogs = Convert.ToInt32(txtTurkeyDogs.Text)

        'Calculate total number of hot dogs ordered
        intNumTotalDogs = intNumBeefDogs + intNumPorkDogs + intNumTurkeyDogs

        'Calculate subtotal, sales tax, and total amounts
        dblSubTotal = intNumTotalDogs * DBL_DRONE_DOG_PRICE
        dblTotalSalesTax = dblSubTotal * DBL_SALES_TAX_RATE
        dblTotalCost = dblSubTotal + dblTotalSalesTax

        'Convert numbers back to text and display in text boxes
        txtSubtotal.Text = dblSubTotal.ToString("c2")
        txtSalesTax.Text = dblTotalSalesTax.ToString("c2")
        txtTotalCost.Text = dblTotalCost.ToString("c2")



    End Sub

    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click

        'Close form
        Me.Close()

    End Sub

    Private Sub btnSubmit_Click(sender As Object, e As EventArgs) Handles btnSubmit.Click

        'Display message box thanking the user
        MessageBox.Show("Thank you for ordering your meal from DroneDogs")

    End Sub

    Private Sub DroneDogsOrder_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles lblSubtotal.Click

    End Sub
End Class
