package de.wiener234.pack;

public class Point{

    int x, y;

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
    public Point(){
    }

    public void moveTo(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int getX(){
        return this.x;
    }
    public int getY(){
        return this.y;
    }




}
