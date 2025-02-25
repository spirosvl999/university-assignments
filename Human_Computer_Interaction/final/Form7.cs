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
    public partial class Form7 : Form
    {
        public Form7()
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

        private void button6_Click(object sender, EventArgs e)
        {
            pictureBox3.Visible = true;
            MessageBox.Show("StairCase Opened!");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            comboBox1.Visible = true;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if(comboBox1.SelectedIndex == 0)
            {
                MessageBox.Show("Door is fully CLOSED!");
            }
            else if(comboBox1.SelectedIndex == 1)
            {
                MessageBox.Show("Door is OPENED MIDWAYS!");
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                MessageBox.Show("Door is fully OPENED!");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.pictureBox2.Top = this.pictureBox2.Top - 2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.pictureBox2.Top = this.pictureBox2.Top + 2;
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            Form8 f8 = new Form8();
            f8.ShowDialog();
            MessageBox.Show("That's the map zoomed!");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.pictureBox2.Left = this.pictureBox2.Left - 2;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.pictureBox2.Left = this.pictureBox2.Left + 2;
        }
    }
}
