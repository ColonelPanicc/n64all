package com.github.georgeprice.n64android;

import android.annotation.SuppressLint;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

//    private static final String SERVER_PATH_GET_ID = "https://n64all.herokuapp.com/join";
//    private static final String SERVER_PATH_LEAVE = "https://n64all.herokuapp.com/leave";
//    private static final String SERVER_PATH_UPDATE_STATE = "https://n64all.herokuapp.com/update";
    private static final String SERVER_PATH_GET_ID = "http://10.245.8.174:8000/join";
    private static final String SERVER_PATH_LEAVE = "http://10.245.8.174:8000/leave";
    private static final String SERVER_PATH_UPDATE_STATE = "http://10.245.8.174:8000/update";

    private OkHttpClient okHttpClient;
    private TextView txtMyId;

    private int myId = -1;

    SensorManager mSensorManager;
    Sensor mSensor;

    @SuppressLint("SetTextI18n")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        okHttpClient = new OkHttpClient();

        txtMyId = findViewById(R.id.txtMyId);
        txtMyId.setText("Player ID: ?");

        mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        mSensor = mSensorManager.getDefaultSensor(Sensor.TYPE_GRAVITY);

        mSensorManager.registerListener(new SensorEventListener() {
            @Override
            public void onSensorChanged(SensorEvent sensorEvent) {
                new Thread(() -> {
                    try {
                        float val = sensorEvent.values[1]; // Y Axis is values[1]

                        final MediaType TEXT = MediaType.parse("text/plain; charset=utf-8");

                        JSONObject json = new JSONObject();
                        json.put("ANALOG", new int[] {(int)Math.round(val * 12.7), 0});
                        json.put("A_BTN", 0);
                        json.put("B_BTN", 0);
                        json.put("Z_BTN", 0);
                        json.put("C_UP_ARROW", 0);
                        json.put("C_LEFT_ARROW", 0);
                        json.put("C_RIGHT_ARROW", 0);
                        json.put("C_DOWN_ARROW", 0);
                        json.put("L_TRIGGER", 0);
                        json.put("R_TRIGGER", 0);
                        json.put("START", 0);
                        JSONObject outer = new JSONObject();
                        outer.put("" + myId, json);

                        RequestBody body = RequestBody.create(TEXT, outer.toString());
                        Request request = new Request.Builder()
                                .url(SERVER_PATH_UPDATE_STATE)
                                .post(body)
                                .build();
                        Response response = okHttpClient.newCall(request).execute();
                        response.body().string();
                    } catch (JSONException | IOException e) {
                        e.printStackTrace();
                    }

                }).start();
            }

            @Override
            public void onAccuracyChanged(Sensor sensor, int i) {

            }
        }, mSensor, 99000);
    }

    @Override
    protected void onPause() {
        super.onPause();
        new Thread(() -> {
            try {
                final MediaType TEXT = MediaType.parse("text/plain; charset=utf-8");

                JSONObject json = new JSONObject();
                json.put("player_id", myId);

                RequestBody body = RequestBody.create(TEXT, json.toString());
                Request request = new Request.Builder()
                        .url(SERVER_PATH_LEAVE)
                        .post(body)
                        .build();
                Response response = okHttpClient.newCall(request).execute();
                response.body().string();
            } catch (IOException | JSONException e) {
                e.printStackTrace();
            }

        }).start();
    }

    @SuppressLint("SetTextI18n")
    @Override
    protected void onResume() {
        super.onResume();
        new Thread(() -> {
            try {
                Request request = new Request.Builder()
                        .url(SERVER_PATH_GET_ID)
                        .build();

                try (Response response = okHttpClient.newCall(request).execute()) {
                    myId = Integer.parseInt(new JSONObject(response.body().string()).getString("success"));
                    txtMyId.post(() -> txtMyId.setText("Player ID: " + myId));
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            } catch (NullPointerException | IOException e) {
                e.printStackTrace();
            }
        }).start();
    }
}
