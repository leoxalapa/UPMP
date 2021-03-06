
package pkg7proyectoconjuntos;

import java.util.Scanner;


public class Operaciones {
    int[] A;
    int[] B;
    
    public void ejecutar(){
        crear();
        union(A,B);
        System.out.println();
        interseccion(A,B);
        System.out.println();
        diferencia(A,B);
        System.out.println();
        potencia(A);
        System.out.println();
    }
    
    public void crear(){
        int t1;
        int t2;
        Scanner leer = new Scanner(System.in);
        
        System.out.println("Ingrese tamaño de A");
        t1 = leer.nextInt();
        System.out.println("Ingrese tamaño de B");
        t2 = leer.nextInt();
        
        A = new int[t1];
        B = new int[t2];
        
        A = leer(t1,'A');
        B = leer(t2,'B');
        
    }
    
    public int[] leer(int t, char nom){
        int[] arre = new int[t];
        Scanner leer = new Scanner(System.in);
        
        for(int i=0;i<arre.length;i++){
            System.out.println("Ingrese valor "+(i+1)+" de "+nom);
            arre[i] = leer.nextInt();
        }  
        return arre;
    }
    
    public boolean pertenece(int x,int[] q){
        boolean p=false;
        
        for(int i=0;i<q.length;i++){
            if(x==q[i]){
                p=true;
            }
        }
        return p;
        
    }
    
    public void union(int[] p, int[] q){
        int[] c = new int[p.length+q.length];
        int cont = 0;
        int j = 0;
        
        for(int i=0;i<p.length;i++){
            if(pertenece(p[i], q)){
                cont++;
            }else{
                c[j] = p[i]; 
                j++;
            }
        }
        
        for(int i=0;i<q.length;i++){
            c[j] = q[i]; 
            j++;
        }
        
        int[] aux = new int[c.length-cont];
        for(int i=0;i<aux.length;i++){
            aux[i]=c[i];
        }
        
        imprimir(aux);
        
    }
    
    public void interseccion(int[] p, int[] q){
        int[] c;
        int j=0;
        
        if(p.length<=q.length){
            c = new int[p.length];
        }else{
            c = new int[q.length];
        }
        
        for(int i=0;i<p.length;i++){
            if(pertenece(p[i],q)){
                c[j] = p[i];
                j++;
            }
        }
        int[] aux = new int[j];
        for(int i=0;i<j;i++){
            aux[i] = c[i];
        }
        imprimir(aux);
        
        
        
    }
    
    public void diferencia(int[] p, int[] q){
        int[] c;
        int j=0;
        
        if(p.length<=q.length){
            c = new int[p.length];
        }else{
            c = new int[q.length];
        }
        
        for(int i=0;i<p.length;i++){
            if(!pertenece(p[i],q)){
                c[j] = p[i];
                j++;
            }
        }
        int[] aux = new int[j];
        for(int i=0;i<j;i++){
            aux[i] = c[i];
        }
        imprimir(aux);
        
    }
    
    public void potencia(int[] p){
        int[][] c;
        int tam;
        tam = (int)(Math.pow(2,p.length));
        c = new int[tam][];
        
        c[0] = new int[]{};
        
        
        System.out.print("{");
        for(int i=0;i<c.length;i++){
            imprimir(c[i]);
            if(i<(c.length-1)){
                System.out.print(", ");
            }    
        }
        System.out.print("}");
    
    }
    
    public void imprimir(int[] q){
        System.out.print("{");
        for(int i=0;i<q.length;i++){
            System.out.print(q[i]);
            if(i<(q.length-1)){
                System.out.print(", ");
            }    
        }
        System.out.print("}");
    }
    
}
