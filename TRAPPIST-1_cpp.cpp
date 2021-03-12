#include <bits/stdc++.h>
#define Pi 3.14159265359  
using namespace std;

int main(){
	
	const int Nb = 8;//���������� ��� � �������
	int Time = 2;//����� � ������
	float dt = 0.000001;//��� 5 ���
	int N_steps = Time/dt;//���������� ��������
	float G = 8.89042 * pow(10, -10);//�������������� ����������
	int i, k, z;
	float sumx = 0, sumy = 0, Ek = 0, Ep = 0, E = 0;
	
	const float m[Nb] = {29600, 0.79, 1.63, 0.33, 0.24, 0.4, 0.566, 0.04};
	const float r[Nb] = {0.0, 0.0115, 0.01576, 0.02219, 0.02916, 0.03836, 0.0467, 0.0617};
	float phase[Nb] = {0.0, 0.0, 217.470, 300.378, 142.558, 323.471, 269.932, 42.487};
	const float T[Nb] = {1.0, 1.51087637, 2.42180746, 4.049959, 6.099043, 9.205585, 12.354473, 18.767953};
	
	float pos[Nb][2];
	float vx[Nb]; float vy[Nb];
	//��������� ������ ��� ������ ��������� � �������+����� � �����
	ofstream f;
	ofstream e;
	//��������� ����� � ������ ������, ios:out - ����� ��������
	f.open("D:\\XYout.txt", ios::out);
	e.open("D:\\Energy.txt", ios::out);
	//������������� ��������� ���� � �������
	for (i = 0; i < Nb; i++){
		phase[i] *= Pi/180;
	}
	//������������ ��������� �������� � ��������� ������
	for (i = 0; i < Nb; i++){
		pos[i][0] = r[i]*cos(phase[i]);
		pos[i][1] = r[i]*sin(phase[i]);
		vx[i] = -(2*r[i]*Pi/T[i]*sin(phase[i]));
		vy[i] = 2*r[i]*Pi/T[i]*cos(phase[i]);
		f << pos[i][0] << " " << pos[i][1] << " ";
	}
	f << endl;
	int step = 1;
	while (step <= N_steps){
		//������ ������ ����
		for (i = 0; i < Nb; i++){
			//������� ������������ ������� ������� i-�� ����
			Ek = m[i]*(pow(vx[i], 2) + pow(vy[i], 2))/2;
			E += Ek;
			//������ ���� �� ������ � ������� 2-�� �-�� ������� 
			//� ������������� ������� ��� i-�� ����
			for (k = 0; k < Nb; k++){
				if (k == i) continue;
				sumx += m[k]*(pos[k][0]-pos[i][0])/(pow(pow(pos[k][0]-pos[i][0], 2) + pow(pos[k][1]-pos[i][1], 2), 1.5));
				sumy += m[k]*(pos[k][1]-pos[i][1])/(pow(pow(pos[k][0]-pos[i][0], 2) + pow(pos[k][1]-pos[i][1], 2), 1.5));
				Ep -= 0.5*G*m[i]*m[k]/sqrt(pow(pos[k][0]-pos[i][0], 2) + pow(pos[k][1]-pos[i][1], 2));
			}
			//�������� ���������
			pos[i][0] += vx[i]*dt;
			pos[i][1] += vy[i]*dt;
			//������ ������ ��������� � ����
			f << pos[i][0] << " " << pos[i][1] << " ";
			//�������� ���������
			vx[i] += G*sumx*dt;
			vy[i] += G*sumy*dt;
			//�������� ����� �� ������ ��� ���������� ����
			sumx = 0;
			sumy = 0;
		}
		f << endl;
		E += Ep;
		e << E << " " << step << endl;
		E = 0; Ep = 0;
		step++;
	}
	//--------------
	f.close();
	e.close();
	return 0;
}
