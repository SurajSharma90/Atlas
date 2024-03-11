using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovementController : MonoBehaviour
{
    [SerializeField]
    Rigidbody2D playerRigidbody2D;

    [SerializeField]
    private float maxVelocity = 5f;

    private void Awake() 
    {
        playerRigidbody2D = GetComponent<Rigidbody2D>();
    }

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        playerRigidbody2D.velocity = new Vector2(
            Input.GetAxis("Horizontal") * maxVelocity, 
            playerRigidbody2D.velocity.y
            );
    }

    private void FixedUpdate()
    {
        
    }
}
