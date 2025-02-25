using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace final
{
    public partial class Form4 : Form
    {
        public Form4()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            Form1 f1 = new Form1();
            f1.ShowDialog();
            this.Close();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            label2.Visible = true;
            label3.Visible = true;
            label4.Visible = true;
            numericUpDown1.Visible = true;
            numericUpDown2.Visible = true;
            button1.Visible = true;
            button3.Visible = true;
            button4.Visible = true;
            button6.Visible = true;
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            if(numericUpDown1.Value > 100)
            {
                numericUpDown1.Value = 100;
                MessageBox.Show("100 % is the maximum amount.");
            }
            else if(numericUpDown1.Value < 0)
            {
                numericUpDown1.Value = 0;
                MessageBox.Show("0 % is the minimum amount.");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(numericUpDown1.Value == 0)
            {
                MessageBox.Show("Pool is Empty!");
            }
            else if(numericUpDown1.Value == 100)
            {
                MessageBox.Show("Pool is Full!");
            }
            else
            {
                MessageBox.Show("Now we have the " + numericUpDown1.Value + " % of pool filled with water.");

            }
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            if(numericUpDown2.Value < 3)
            {
                numericUpDown2.Value = 3;
                MessageBox.Show("3oC is the minimum temperature.");
            }
            else if(numericUpDown2.Value > 55)
            {
                numericUpDown2.Value = 55;
                MessageBox.Show("55oC is the highest temperature.");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Pool's temperature is " + numericUpDown2.Value + " oC");
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void Form4_Load(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Ok the pool's sensor will work at " + dateTimePicker1.ToString());
        }

        private void button4_Click(object sender, EventArgs e)
        {
            button5.Visible = true;
            button6.Visible = false;
            MessageBox.Show("Sensor is ON!");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            button5.Visible = false;
            button6.Visible = true;
            MessageBox.Show("Sensor is OFF!");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            dateTimePicker1.Visible = true;
            button7.Visible = true;
        }
    }
}
