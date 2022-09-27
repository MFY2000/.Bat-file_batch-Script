namespace GitDesktopApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Syb_FocusOn.Top = Btn_Dashborad.Top + getCenter(Btn_Dashborad);
            getDataInilization();
        }

        private void Btn_Dashborad_Click(object sender, EventArgs e)
        {
            Syb_FocusOn.Top = Btn_Dashborad.Top + getCenter(Btn_Dashborad);

        }

        private void Btn_CommitBY_Click(object sender, EventArgs e)
        {
            Syb_FocusOn.Top = Btn_CommitBY.Top + getCenter(Btn_CommitBY);
        }

        private void Btn_Paths_Click(object sender, EventArgs e)
        {
            Syb_FocusOn.Top = Btn_Paths.Top + getCenter(Btn_Paths);
        }

        private int getCenter(Button btn)
        {
            return (btn.Height - Syb_FocusOn.Height) / 2;
             
        }


        private void getDataInilization()
        {
            try
            {
                // your code here 
                string CSVFilePathName = @"C:\Users\DarkJoker\Desktop\Git-Auto-Commit\Git Auto Commit -v2.2.0\GitDesktopApp\Resources\log.csv";
                

                string[] Lines = File.ReadAllLines(CSVFilePathName);
                string[] Fields;
                Fields = Lines[0].Split(new char[] { ',' });
                int Cols = Fields.GetLength(0);

                //1st row must be column names; force lower case to ensure matching later on.
                for (int i = 1; i < Lines.GetLength(0); i++) { 
                    Fields = Lines[i].Split(new char[] { ',' });

                    if (IsRepo(Fields[0]) != 0)
                    {
                        Repo_list.Items.Add(Fields[0]);
                    }
                    else {
                        ErrorRepo.Items.Add(Fields[0]);
                    }               
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error is " + ex.ToString());
                throw;
            }
        }

        private int IsRepo(string path)
        {
            int returnType = 1;

            return returnType;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}