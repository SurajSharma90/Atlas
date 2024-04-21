using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HealthSystem : MonoBehaviour
{
    [Header("Attributes")]
    [SerializeField]
    private int maxHealth = 3;
    private int health = 0;
    //[Space(10)]

    // Start is called before the first frame update
    void Start()
    {
        this.health = this.maxHealth;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void LoseHealth(int amount = 1) 
    {
        this.health -= amount;

        if(this.health <= 0) 
        {
            this.health = 0;
            this.DeathAnimation();
        }
    }

    public void GainHealth(int amount = 1) 
    {
        this.health += amount;

        if (this.health > this.maxHealth)
            this.health = this.maxHealth;
    }

    public bool IsDead() 
    {
        return this.health <= 0 ? true : false;
    }

    private void DeathAnimation() 
    {
        this.gameObject.SetActive(false);
    }
}
