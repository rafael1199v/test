#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double poblacion, nivel_confianza, probabilidad_exito, probabilidad_fracaso, nivel_error, muestra_finita;
    string respuesta;
    //Poblacion = N
    //Nivel de confianza % = z 
    //Probabilidad de exito % = p
    //Probabilidad de fracaso % = q
    //Nivel de error % = e
    do{
        //Se piden los datos al usuario
        cout << "Introduce el valor de la poblacion: "; cin >> poblacion;
        cout << "Introduce el valor del nivel de confianza: "; cin >> nivel_confianza;
        cout << "Introduce el valor de la probabilidad de exito: "; cin >> probabilidad_exito;
        cout << "Introduce el valor de la probabilidad de fracaso: "; cin >> probabilidad_fracaso;
        cout << "Introduce el valor del nivel de error: "; cin >> nivel_error;
        //Se transforma la formula a codigo
        muestra_finita = (pow(nivel_confianza, 2) * probabilidad_exito * probabilidad_fracaso * poblacion)/((pow(nivel_error, 2) * (poblacion - 1)) + (pow(nivel_confianza, 2) * probabilidad_exito * probabilidad_fracaso));
        
         //Redondeamos el valor para que no salgan decimales con la funcion round
        cout << "El valor de la muestra finita es: " << round(muestra_finita) << endl;
        //Preguntamos al usuario si quiere hacer un nuevo calculo
        cout << "Quisieras calcular un nuevo valor? : Si/No" << endl;
        cin >> respuesta;
        
        //Mientras que la respuesta sea igual a "si" y sus variantes, el bucle se va a repetir indefinidamente.
    } while (respuesta == "si" || respuesta == "SI" || respuesta == "Si");
    
    return 0;
}
