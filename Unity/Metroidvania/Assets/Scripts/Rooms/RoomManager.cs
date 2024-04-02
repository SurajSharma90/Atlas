using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RoomManager : MonoBehaviour
{
    [Header("Door Positions")]
    public Transform door_left_pos = null;
    public Transform door_right_pos = null;
    public Transform door_top_pos = null;
    public Transform door_bottom_pos = null;
    [Space(10)]

    [Header("Hallway Positions")]
    public Transform hallway_left_pos = null;
    public Transform hallway_right_pos = null;
    public Transform hallway_top_pos = null;
    public Transform hallway_bottom_pos = null;
    [Space(10)]

    [Header("Room References")]
    public GameObject room_left = null;
    public GameObject room_right = null;
    public GameObject room_top = null;
    public GameObject room_bottom = null;
    [Space(10)]

    [Header("Hallway References")]
    public GameObject hallway_left = null;
    public GameObject hallway_right = null;
    public GameObject hallway_top = null;
    public GameObject hallway_bottom = null;

    private void Awake()
    {
        
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
