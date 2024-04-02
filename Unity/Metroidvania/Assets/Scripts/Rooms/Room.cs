using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Room : MonoBehaviour
{
    [Header("Door Positions")]
    public Transform door_left_pos = null;
    public Transform door_right_pos = null;
    public Transform door_top_pos = null;
    public Transform door_bottom_pos = null;
    [Space(10)]

    [Header("Room Positions")]
    public Transform room_left_pos = null;
    public Transform room_right_pos = null;
    public Transform room_top_pos = null;
    public Transform room_bottom_pos = null;
    [Space(10)]

    [Header("Door References")]
    public GameObject door_left = null;
    public GameObject door_right = null;
    public GameObject door_top = null;
    public GameObject door_bottom = null;
    [Space(10)]

    [Header("Room References")]
    public GameObject room_left = null;
    public GameObject room_right = null;
    public GameObject room_top = null;
    public GameObject room_bottom = null;

    private void Awake()
    {
        
    }

    // Start is called before the first frame update
    void Start()
    {
        this.CreateDoors();
    }
    // Update is called once per frame
    void Update()
    {
        
    }

    public void CreateDoors()
    {
        
    }
}
