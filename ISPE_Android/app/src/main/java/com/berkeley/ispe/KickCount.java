package com.berkeley.ispe;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import java.util.Timer;
import java.util.TimerTask;

public class KickCount extends AppCompatActivity {
    private Button buttonCount;
    private TextView textViewHours, textViewMinutes;
    int minutes = 0;
    int hours = 0;
    int kickCount = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_kick_count);
        setup();
        final int sekundi = 0 ;
        Timer timer = new Timer();
        TimerTask t = new TimerTask() {
            int sec = 0;
            @Override
            public void run() {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if(minutes == 60){
                            hours += 1;
                            minutes = 0;
                        } else{
                            minutes += 1;
                        }
                        kickCount = minutes;
                        setTexts();
                    }
                });
            }
        };
        timer.scheduleAtFixedRate(t,1000,1000);
    }
    private void setTexts() {
        buttonCount.setText(""+kickCount);
        textViewMinutes.setText(""+minutes);
        textViewHours.setText(""+hours);

    }

    private void setup() {
        buttonCount = (Button)findViewById(R.id.startButton);
        textViewHours = (TextView)findViewById(R.id.hours_number);
        textViewMinutes=(TextView)findViewById(R.id.minutes_number);
    }
}
