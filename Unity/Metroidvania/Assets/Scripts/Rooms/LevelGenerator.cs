using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Tilemaps;

public class LevelGenerator : MonoBehaviour
{
    private enum HALLWAY_TYPE { VERTICAL = 0, HORIZONTAL = 1 };

    [Header("Rooms")]
    [SerializeField]
    private List<GameObject> AvailableRooms;
    [SerializeField]
    private List<GameObject> AvailableVerticalHallways;
    [SerializeField]
    private List<GameObject> AvailableHorizontalHallways;
    private List<GameObject> GeneratedRooms;

    static System.Random random;


    private void Awake()
    {
        random = new System.Random();
        this.GeneratedRooms = new List<GameObject>();
        this.CreateFirstRoom(this.gameObject);
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private GameObject CreateFirstRoom(GameObject grid)
    {
        //Center room
        int index = random.Next(0, AvailableRooms.Count);
        GameObject room = Instantiate(AvailableRooms[index], grid.transform);
        this.GeneratedRooms.Add(room);

        //Create hallway to next room


        return room;
    }

    private GameObject CreateRoom(GameObject parent_hallway)
    {
        //Center room
        int index = random.Next(0, AvailableRooms.Count);
        GameObject room = Instantiate(AvailableRooms[index], parent_hallway.transform);
        this.GeneratedRooms.Add(room);
        RoomManager roomController = room.GetComponent<RoomManager>();

        return room;
    }

    //private GameObject CreateHallway(GameObject parent_room, HALLWAY_TYPE hallway_type)
    //{
    //    if(hallway_type == HALLWAY_TYPE.VERTICAL)
    //    {
    //        //Set references
    //        roomController.hallway_bottom = hallway_bottom;
    //        hallwayManager.parent_room = room;
    //    }

    //    //Connect hallway
    //    int index = random.Next(0, AvailableVerticalHallways.Count);
    //    GameObject hallway_bottom = Instantiate(AvailableVerticalHallways[index], parent_room.transform);
    //    HallwayManager hallwayManager = hallway_bottom.GetComponent<HallwayManager>();
    //    hallway_bottom.transform.position = roomController.hallway_bottom_pos.position - hallwayManager.parent_position.position;
    //}

    private void GenerateRooms()
    {
        GameObject centerRoom = CreateRoom(gameObject);
        GameObject selectedRoom = centerRoom;

        for (int i = 0; i < random.Next(10); i++)
        {
            GameObject room = this.CreateRoom(selectedRoom);
        }

    }
}
