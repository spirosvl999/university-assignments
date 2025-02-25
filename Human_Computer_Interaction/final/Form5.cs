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
    public partial class Form5 : Form
    {
        public decimal total_ammount = 00.00M;
        public Form5()
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
            comboBox1.Visible = true;
            label5.Visible = true;
            button3.Visible = true;
            label22.Visible = true;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox1.SelectedIndex == 0)
            {
                checkedListBox1.Visible = true;
                checkedListBox2.Visible = false;
                checkedListBox3.Visible = false;
                checkedListBox4.Visible = false;
                checkedListBox5.Visible = false;
                label1.Visible = true;
                label2.Visible = true;
                label3.Visible = true;
                label4.Visible = true;
                label6.Visible = false;
                label7.Visible = false;
                label8.Visible = false;
                label9.Visible = false;
                label10.Visible = false;
                label11.Visible = false;
                label12.Visible = false;
                label13.Visible = false;
                label14.Visible = false;
                label15.Visible = false;
                label16.Visible = false;
                label17.Visible = false;
                label18.Visible = false;
                label19.Visible = false;
                label20.Visible = false;
                label21.Visible = false;
                numericUpDown1.Visible = true;
                numericUpDown2.Visible = true;
                numericUpDown3.Visible = true;
                numericUpDown4.Visible = true;
                numericUpDown5.Visible = false;
                numericUpDown6.Visible = false;
                numericUpDown7.Visible = false;
                numericUpDown8.Visible = false;
                numericUpDown9.Visible = false;
                numericUpDown10.Visible = false;
                numericUpDown11.Visible = false;
                numericUpDown12.Visible = false;
                numericUpDown13.Visible = false;
                numericUpDown14.Visible = false;
                numericUpDown15.Visible = false;
                numericUpDown16.Visible = false;
                numericUpDown17.Visible = false;
                numericUpDown18.Visible = false;
                numericUpDown19.Visible = false;
                numericUpDown20.Visible = false;
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                checkedListBox1.Visible = false;
                checkedListBox2.Visible = true;
                checkedListBox3.Visible = false;
                checkedListBox4.Visible = false;
                checkedListBox5.Visible = false;
                label1.Visible = false;
                label2.Visible = false;
                label3.Visible = false;
                label4.Visible = false;
                label6.Visible = true;
                label7.Visible = true;
                label8.Visible = true;
                label9.Visible = true;
                label10.Visible = false;
                label11.Visible = false;
                label12.Visible = false;
                label13.Visible = false;
                label14.Visible = false;
                label15.Visible = false;
                label16.Visible = false;
                label17.Visible = false;
                label18.Visible = false;
                label19.Visible = false;
                label20.Visible = false;
                label21.Visible = false;
                numericUpDown1.Visible = false;
                numericUpDown2.Visible = false;
                numericUpDown3.Visible = false;
                numericUpDown4.Visible = false;
                numericUpDown5.Visible = true;
                numericUpDown6.Visible = true;
                numericUpDown7.Visible = true;
                numericUpDown8.Visible = true;
                numericUpDown9.Visible = false;
                numericUpDown10.Visible = false;
                numericUpDown11.Visible = false;
                numericUpDown12.Visible = false;
                numericUpDown13.Visible = false;
                numericUpDown14.Visible = false;
                numericUpDown15.Visible = false;
                numericUpDown16.Visible = false;
                numericUpDown17.Visible = false;
                numericUpDown18.Visible = false;
                numericUpDown19.Visible = false;
                numericUpDown20.Visible = false;
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                checkedListBox1.Visible = false;
                checkedListBox2.Visible = false;
                checkedListBox3.Visible = true;
                checkedListBox4.Visible = false;
                checkedListBox5.Visible = false;
                label1.Visible = false;
                label2.Visible = false;
                label3.Visible = false;
                label4.Visible = false;
                label6.Visible = false;
                label7.Visible = false;
                label8.Visible = false;
                label9.Visible = false;
                label10.Visible = true;
                label11.Visible = true;
                label12.Visible = true;
                label13.Visible = true;
                label14.Visible = false;
                label15.Visible = false;
                label16.Visible = false;
                label17.Visible = false;
                label18.Visible = false;
                label19.Visible = false;
                label20.Visible = false;
                label21.Visible = false;
                numericUpDown1.Visible = false;
                numericUpDown2.Visible = false;
                numericUpDown3.Visible = false;
                numericUpDown4.Visible = false;
                numericUpDown5.Visible = false;
                numericUpDown6.Visible = false;
                numericUpDown7.Visible = false;
                numericUpDown8.Visible = false;
                numericUpDown9.Visible = true;
                numericUpDown10.Visible = true;
                numericUpDown11.Visible = true;
                numericUpDown12.Visible = true;
                numericUpDown13.Visible = false;
                numericUpDown14.Visible = false;
                numericUpDown15.Visible = false;
                numericUpDown16.Visible = false;
                numericUpDown17.Visible = false;
                numericUpDown18.Visible = false;
                numericUpDown19.Visible = false;
                numericUpDown20.Visible = false;
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                checkedListBox1.Visible = false;
                checkedListBox2.Visible = false;
                checkedListBox3.Visible = false;
                checkedListBox4.Visible = true;
                checkedListBox5.Visible = false;
                label1.Visible = false;
                label2.Visible = false;
                label3.Visible = false;
                label4.Visible = false;
                label6.Visible = false;
                label7.Visible = false;
                label8.Visible = false;
                label9.Visible = false;
                label10.Visible = false;
                label11.Visible = false;
                label12.Visible = false;
                label13.Visible = false;
                label14.Visible = true;
                label15.Visible = true;
                label16.Visible = true;
                label17.Visible = true;
                label18.Visible = false;
                label19.Visible = false;
                label20.Visible = false;
                label21.Visible = false;
                numericUpDown1.Visible = false;
                numericUpDown2.Visible = false;
                numericUpDown3.Visible = false;
                numericUpDown4.Visible = false;
                numericUpDown5.Visible = false;
                numericUpDown6.Visible = false;
                numericUpDown7.Visible = false;
                numericUpDown8.Visible = false;
                numericUpDown9.Visible = false;
                numericUpDown10.Visible = false;
                numericUpDown11.Visible = false;
                numericUpDown12.Visible = false;
                numericUpDown13.Visible = true;
                numericUpDown14.Visible = true;
                numericUpDown15.Visible = true;
                numericUpDown16.Visible = true;
                numericUpDown17.Visible = false;
                numericUpDown18.Visible = false;
                numericUpDown19.Visible = false;
                numericUpDown20.Visible = false;
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                checkedListBox1.Visible = false;
                checkedListBox2.Visible = false;
                checkedListBox3.Visible = false;
                checkedListBox4.Visible = false;
                checkedListBox5.Visible = true;
                label1.Visible = false;
                label2.Visible = false;
                label3.Visible = false;
                label4.Visible = false;
                label6.Visible = false;
                label7.Visible = false;
                label8.Visible = false;
                label9.Visible = false;
                label10.Visible = false;
                label11.Visible = false;
                label12.Visible = false;
                label13.Visible = false;
                label14.Visible = false;
                label15.Visible = false;
                label16.Visible = false;
                label17.Visible = false;
                label18.Visible = true;
                label19.Visible = true;
                label20.Visible = true;
                label21.Visible = true;
                numericUpDown1.Visible = false;
                numericUpDown2.Visible = false;
                numericUpDown3.Visible = false;
                numericUpDown4.Visible = false;
                numericUpDown5.Visible = false;
                numericUpDown6.Visible = false;
                numericUpDown7.Visible = false;
                numericUpDown8.Visible = false;
                numericUpDown9.Visible = false;
                numericUpDown10.Visible = false;
                numericUpDown11.Visible = false;
                numericUpDown12.Visible = false;
                numericUpDown13.Visible = false;
                numericUpDown14.Visible = false;
                numericUpDown15.Visible = false;
                numericUpDown16.Visible = false;
                numericUpDown17.Visible = true;
                numericUpDown18.Visible = true;
                numericUpDown19.Visible = true;
                numericUpDown20.Visible = true;
            }
        }

        private void checkedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        { 
            Form6 f6 = new Form6();
            f6.ShowDialog();
        }

        private void Form5_Load(object sender, EventArgs e)
        {

        }

        private void numericUpDown20_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (6.99M * numericUpDown20.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown19_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (13.99m * numericUpDown19.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown18_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (9.99M * numericUpDown18.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown17_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (120 * numericUpDown17.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown16_ValueChanged_1(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (1.99M * numericUpDown16.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown12_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (3.99M * numericUpDown12.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown8_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (8.99M * numericUpDown8.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (5.99M * numericUpDown1.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown15_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (1.99M * numericUpDown15.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown11_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (2.99M * numericUpDown11.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown7_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (10.99M * numericUpDown7.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (7.99M * numericUpDown2.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown3_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (7.99M * numericUpDown3.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown6_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (9.99M * numericUpDown6.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown10_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (2.49M * numericUpDown10.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown14_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (1.99M * numericUpDown14.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown4_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (3.99M * numericUpDown4.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown5_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (6.99M * numericUpDown5.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown9_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (3.99M * numericUpDown9.Value));
            label22.Text = ("" + total_ammount);
        }

        private void numericUpDown13_ValueChanged(object sender, EventArgs e)
        {
            total_ammount = (total_ammount + (0.49M * numericUpDown13.Value));
            label22.Text = ("" + total_ammount);
        }
    }
}