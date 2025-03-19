import promptSync from 'prompt-sync';

// Inicializar prompt-sync
const prompt = promptSync();

// ----------------- CONSIGNA ----------------- 
// Crear un programa donde se ingresen datos de varias personas (nombre, edad, nota).  
// Al finalizar el programa por alguna opcion ( finalizar o terminado ) 
// mostrar el listado completo de datos cargados y otro listado ordenado por nota de mayor a menor.   

// ----------------- DESARROLLO -----------------

// Ingresar cantidad de usuarios
const PERSONAS_REGISTRADAS = [];

const usuarios_a_registrar = parseInt(prompt("Ingrese una cantidad total de usuarios para el registro!: "));

// Iteramos sobre cada input
for (let _ = 0; _ < usuarios_a_registrar; _++) {
    // INPUTS DE USUARIOS
    const nombre = prompt("Ingresa tu nombre: ");
    const edad = parseInt(prompt("ingresar tu edad: "));
    const nota = parseFloat(prompt("nota: "));
    
    const datos_personas = [nombre, edad, nota];
    PERSONAS_REGISTRADAS.push(datos_personas);
    
    console.log(`${nombre} tiene ${edad} de años!, y su nota actual es de: ${nota}`);
}

console.log("\nListado completo:");
PERSONAS_REGISTRADAS.forEach(p => {
    console.log(`Nombre: ${p[0]}, Edad: ${p[1]}, Nota: ${p[2]}`, p);
});

console.log("\nListado ordenado por nota (mayor a menor):");
const notas_ordenadas_mayor_menor = [...PERSONAS_REGISTRADAS].sort((a, b) => b[2] - a[2]);

notas_ordenadas_mayor_menor.forEach(p => {
    console.log(`Nombre: ${p[0]}, Nota: ${p[2]}`);
});