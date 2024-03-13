using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovementController : MonoBehaviour
{
    [SerializeField]
    Rigidbody2D playerRigidbody2D;
    [SerializeField]
    private float jumpForce = 12f;
    [SerializeField]
    private Transform bottomCollisionPoint = null;
    private bool isGround = true;
    [SerializeField]
    private LayerMask tileLayer;

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
        isGround = Physics2D.OverlapCircle(bottomCollisionPoint.position, .2f, tileLayer);

        if(Input.GetButtonDown("Jump") && isGround == true) 
        {
            isGround = false;
            playerRigidbody2D.velocity = new Vector2(
                playerRigidbody2D.velocity.x, 
                jumpForce
                );
        }
        
        playerRigidbody2D.velocity = new Vector2(
            Input.GetAxis("Horizontal") * maxVelocity, 
            playerRigidbody2D.velocity.y
            );
    }

    private void FixedUpdate()
    {
        
    }
}
