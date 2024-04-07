using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class CharacterController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField]
    private Rigidbody2D playerRigidbody2D = null;
    [SerializeField]
    private float maxVelocity = 1.0f;
    [Space(10)]

    [Header("Animation")]
    [SerializeField]
    private Animator playerAnimator = null;
    [Space(10)]

    //New input
    [Header("Input")]
    private BasicInput input = null;
    private Vector2 moveVector = Vector2.zero;

    private void Awake()
    {
        if(input == null)
            input = new BasicInput();

        if(playerRigidbody2D == null)
            playerRigidbody2D = GetComponent<Rigidbody2D>();

        if (playerAnimator == null)
            playerAnimator = GetComponent<Animator>();

        //QualitySettings.vSyncCount = 0;  // VSync must be disabled
        //Application.targetFrameRate = 20;
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //playerRigidbody2D.velocity = new Vector2(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical")) * maxVelocity;
        //playerRigidbody2D.velocity = moveVector * maxVelocity;
        //playerRigidbody2D.AddForce(moveVector * maxVelocity * Time.deltaTime);
        //Debug.Log(moveVector);
    }

    private void LateUpdate()
    {
        if(playerAnimator != null )
        {
            playerAnimator.SetFloat("xVelocity", playerRigidbody2D.velocity.x);
            playerAnimator.SetFloat("yVelocity", playerRigidbody2D.velocity.y);
        }
    }

    private void FixedUpdate()
    {
        playerRigidbody2D.AddForce(moveVector * maxVelocity * Time.deltaTime);
    }

    private void OnEnable()
    {
        input.Enable();
        input.Player.Keyboard_Movement.performed += OnMovementPerformed;
        input.Player.Keyboard_Movement.canceled += OnMovementCancelled;
    }

    private void OnDisable()
    {
        input.Disable();
        input.Player.Keyboard_Movement.performed -= OnMovementPerformed;
        input.Player.Keyboard_Movement.canceled -= OnMovementCancelled;
    }

    private void OnMovementPerformed(InputAction.CallbackContext value)
    {
        moveVector = value.ReadValue<Vector2>();
    }

    private void OnMovementCancelled(InputAction.CallbackContext value)
    {
        moveVector = Vector2.zero;
    }
}
