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
    public partial class Form3 : Form
    {
        public Form3()
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

        private void button1_Click(object sender, EventArgs e)
        {
            label2.Visible = true;
            label3.Visible = true;
            label4.Visible = true;
            button3.Visible = true;
            button4.Visible = true;
            button6.Visible = true;
            button7.Visible = true;
            button8.Visible = true;
            comboBox1.Visible = true;
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            MessageBox.Show(comboBox1.SelectedItem + " turned ON!");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            MessageBox.Show(comboBox1.SelectedItem + " turned OFF!");
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form3_Load(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Room's Lights Turned ON!");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Room's Lights Turned OFF!");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            button5.Visible = true;
            button9.Visible = true;
            numericUpDown1.Visible = true;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            
            MessageBox.Show("Room's temperature setted up to " + numericUpDown1.Value);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            button5.Visible = false;
            button9.Visible = false;
            numericUpDown1.Visible = false;
            MessageBox.Show("Heating is OFF.");
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            if (numericUpDown1.Value <= 15)
            {
                numericUpDown1.Value = 16;
            }
            else if (numericUpDown1.Value >= 30)
            {
                numericUpDown1.Value = 29;
            }
        }
    }
}